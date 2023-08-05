from datetime import datetime
from io import StringIO

import tzlocal
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GroupMessageEvent
from nonebot.internal.matcher import Matcher

from nonebot_plugin_mahjong_scoreboard.controller.general_handlers import require_group_binding_qq, \
    require_parse_unary_text_arg
from nonebot_plugin_mahjong_scoreboard.controller.interceptor import general_interceptor
from nonebot_plugin_mahjong_scoreboard.controller.mapper.game_csv_mapper import map_games_as_csv
from nonebot_plugin_mahjong_scoreboard.errors import BadRequestError
from nonebot_plugin_mahjong_scoreboard.model.enums import SeasonState
from nonebot_plugin_mahjong_scoreboard.service import season_service, game_service
from nonebot_plugin_mahjong_scoreboard.service.group_service import get_group_by_binding_qq
from nonebot_plugin_mahjong_scoreboard.utils.date import encode_date
from nonebot_plugin_mahjong_scoreboard.utils.upload_file import upload_group_file, upload_private_file

# ========== 导出赛季对局 ==========
export_season_games_matcher = on_command("导出赛季对局", aliases={"导出对局"}, priority=5)

require_parse_unary_text_arg(export_season_games_matcher, "season_code")
require_group_binding_qq(export_season_games_matcher)


@export_season_games_matcher.handle()
@general_interceptor(export_season_games_matcher)
async def export_season_games(bot: Bot, event: MessageEvent, matcher: Matcher):
    group = await get_group_by_binding_qq(matcher.state["binding_qq"])

    season_code = matcher.state.get("season_code", None)
    if season_code:
        season = await season_service.get_season_by_code(season_code, group)
        if season is None:
            raise BadRequestError("找不到指定赛季")
    else:
        if group.running_season_id:
            season = await season_service.get_season_by_id(group.running_season_id)
        else:
            raise BadRequestError("当前没有运行中的赛季")

    games = await game_service.get_games(season=season)

    filename = f"赛季对局 {season.name}"
    if season.state == SeasonState.finished:
        filename += "（已结束）"
    else:
        now = datetime.now(tzlocal.get_localzone())
        filename += f"（截至{encode_date(now)}）"
    filename += ".csv"

    with StringIO() as sio:
        await map_games_as_csv(sio, games)

        data = sio.getvalue().encode("utf_8_sig")
        if isinstance(event, GroupMessageEvent):
            await upload_group_file(bot, event.group_id, filename, data)
        else:
            await upload_private_file(bot, event.user_id, filename, data)


# ========== 导出所有对局 ==========
export_group_games_matcher = on_command("导出所有对局", priority=5)

require_group_binding_qq(export_group_games_matcher)


@export_group_games_matcher.handle()
@general_interceptor(export_group_games_matcher)
async def export_group_games(bot: Bot, event: MessageEvent, matcher: Matcher):
    group = await get_group_by_binding_qq(matcher.state["binding_qq"])
    games = await game_service.get_games(group)

    now = datetime.now(tzlocal.get_localzone())
    filename = f"所有对局（截至{encode_date(now)}）.csv"

    with StringIO() as sio:
        await map_games_as_csv(sio, games)

        data = sio.getvalue().encode("utf_8_sig")
        if isinstance(event, GroupMessageEvent):
            await upload_group_file(bot, event.group_id, filename, data)
        else:
            await upload_private_file(bot, event.user_id, filename, data)
