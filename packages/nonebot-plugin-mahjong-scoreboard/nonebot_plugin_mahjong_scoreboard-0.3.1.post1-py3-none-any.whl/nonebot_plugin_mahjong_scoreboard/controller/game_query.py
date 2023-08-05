from datetime import date, timedelta, datetime, time

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment, MessageEvent
from nonebot.internal.matcher import Matcher

from nonebot_plugin_mahjong_scoreboard.controller.context import save_context
from nonebot_plugin_mahjong_scoreboard.controller.general_handlers import require_parse_unary_at_arg, \
    require_game_code_from_context, require_parse_unary_integer_arg, require_group_binding_qq, require_user_binding_qq
from nonebot_plugin_mahjong_scoreboard.controller.interceptor import general_interceptor
from nonebot_plugin_mahjong_scoreboard.controller.mapper.game_mapper import map_game
from nonebot_plugin_mahjong_scoreboard.controller.utils.send_messages import send_msgs
from nonebot_plugin_mahjong_scoreboard.errors import BadRequestError
from nonebot_plugin_mahjong_scoreboard.service import group_service, game_service
from nonebot_plugin_mahjong_scoreboard.service.group_service import get_group_by_binding_qq
from nonebot_plugin_mahjong_scoreboard.service.user_service import get_user_by_binding_qq

# =============== 查询对局 ===============
query_by_code_matcher = on_command("查询对局", aliases={"对局"}, priority=5)

require_game_code_from_context(query_by_code_matcher)
require_parse_unary_integer_arg(query_by_code_matcher, "game_code")
require_group_binding_qq(query_by_code_matcher)


@query_by_code_matcher.handle()
@general_interceptor(query_by_code_matcher)
async def query_by_code(matcher: Matcher):
    game_code = matcher.state.get("game_code", None)
    if game_code is None:
        raise BadRequestError("请指定对局编号")

    group = await group_service.get_group_by_binding_qq(matcher.state["binding_qq"])
    game = await game_service.get_game_by_code(game_code, group)
    if game is None:
        raise BadRequestError("未找到指定对局")

    msg = await map_game(game, detailed=True)
    send_result = await matcher.send(msg)
    save_context(send_result["message_id"], game_code=game.code)


# ========== 个人最近对局 ==========
query_user_recent_games_matcher = on_command("个人最近对局", aliases={"最近对局"}, priority=5)

require_parse_unary_at_arg(query_user_recent_games_matcher, "user_binding_qq")
require_group_binding_qq(query_user_recent_games_matcher)
require_user_binding_qq(query_user_recent_games_matcher)


@query_user_recent_games_matcher.handle()
@general_interceptor(query_user_recent_games_matcher)
async def query_user_recent_games(bot: Bot, event: MessageEvent, matcher: Matcher):
    group_binding_qq = matcher.state["binding_qq"]
    user_binding_qq = matcher.state["user_binding_qq"]

    group = await get_group_by_binding_qq(group_binding_qq)
    user = await get_user_by_binding_qq(user_binding_qq)

    end_time = datetime.combine(date.today() + timedelta(days=1), time())
    start_time = datetime.combine(end_time - timedelta(days=7), time())

    games = await game_service.get_games(group, user, limit=30, reverse_order=True, time_span=(start_time, end_time))
    if len(games) != 0:
        member_info = await bot.get_group_member_info(group_id=group.binding_qq, user_id=user.binding_qq)
        header = Message([
            MessageSegment.text("以下是"),
            MessageSegment("at", {"qq": user.binding_qq, "name": member_info["nickname"]}),
            MessageSegment.text("的最近对局")
        ])
        messages = [header]
        for g in games:
            messages.append(await map_game(g, detailed=True))

        await send_msgs(bot, event, messages)
    else:
        await matcher.send("你还没有进行过对局")


# ========== 群最近对局 ==========
query_group_recent_games_matcher = on_command("群最近对局", priority=5)

require_group_binding_qq(query_group_recent_games_matcher)


@query_group_recent_games_matcher.handle()
@general_interceptor(query_group_recent_games_matcher)
async def query_group_recent_games(bot: Bot, event: MessageEvent, matcher: Matcher):
    group = await get_group_by_binding_qq(matcher.state["binding_qq"])

    end_time = datetime.combine(date.today() + timedelta(days=1), time())
    start_time = datetime.combine(end_time - timedelta(days=7), time())

    games = await game_service.get_games(group, limit=30, reverse_order=True, time_span=(start_time, end_time))
    if len(games) != 0:
        header = Message(MessageSegment.text("以下是本群的最近对局"))
        messages = [header]
        for g in games:
            messages.append(await map_game(g, detailed=True))

        await send_msgs(bot, event, messages)
    else:
        await matcher.send("本群还没有进行过对局")


# ========== 个人未完成对局 ==========
query_user_uncompleted_games_matcher = on_command("个人未完成对局", aliases={"未完成对局"}, priority=5)

require_parse_unary_at_arg(query_user_uncompleted_games_matcher, "user_binding_qq")
require_group_binding_qq(query_user_uncompleted_games_matcher)
require_user_binding_qq(query_user_uncompleted_games_matcher)


@query_user_uncompleted_games_matcher.handle()
@general_interceptor(query_user_uncompleted_games_matcher)
async def query_user_uncompleted_games(bot: Bot, event: MessageEvent, matcher: Matcher):
    group_binding_qq = matcher.state["binding_qq"]
    user_binding_qq = matcher.state["user_binding_qq"]

    group = await get_group_by_binding_qq(group_binding_qq)
    user = await get_user_by_binding_qq(user_binding_qq)

    games = await game_service.get_games(group, user, uncompleted_only=True, limit=30, reverse_order=True)
    if len(games) != 0:
        member_info = await bot.get_group_member_info(group_id=group.binding_qq, user_id=user.binding_qq)
        header = Message([
            MessageSegment.text("以下是"),
            MessageSegment("at", {"qq": user.binding_qq, "name": member_info["nickname"]}),
            MessageSegment.text("的未完成对局")
        ])

        messages = [header]
        for g in games:
            messages.append(await map_game(g, detailed=True))

        await send_msgs(bot, event, messages)
    else:
        await matcher.send("你还没有未完成的对局")


# ========== 群未完成对局 ==========
query_group_uncompleted_games_matcher = on_command("群未完成对局", priority=5)

require_group_binding_qq(query_group_uncompleted_games_matcher)


@query_group_uncompleted_games_matcher.handle()
@general_interceptor(query_group_uncompleted_games_matcher)
async def query_group_uncompleted_games(bot: Bot, event: MessageEvent, matcher: Matcher):
    group_binding_qq = matcher.state["binding_qq"]

    group = await get_group_by_binding_qq(group_binding_qq)

    games = await game_service.get_games(group, uncompleted_only=True, limit=30, reverse_order=True)
    if len(games) != 0:
        header = Message(MessageSegment.text("以下是本群的未完成对局"))
        messages = [header]
        for g in games:
            messages.append(await map_game(g, detailed=True))

        await send_msgs(bot, event, messages)
    else:
        await matcher.send("本群还没有未完成的对局")
