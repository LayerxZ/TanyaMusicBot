from asyncio import QueueEmpty
from config import que
from database.queue import (
    is_active_chat,
    add_active_chat,
    remove_active_chat,
    music_on,
    is_music_playing,
    music_off,
)
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from callsmusic import callsmusic
from callsmusic.queues.queues import clear, get, is_empty, put, task_done
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


@Client.on_message(command(["pause", "jeda"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    checking = message.from_user.mention
    chat_id = message.chat.id
    if not await is_active_chat(chat_id):
        return await message.reply_text(
            "I dont think if something's playing on voice chat"
        )
    elif not await is_music_playing(message.chat.id):
        return await message.reply_text(
            "I dont think if something's playing on voice chat"
        )
    await music_off(chat_id)
    await callsmusic.pytgcalls.pause_stream(chat_id)
    await message.reply_text(f"🎧 Voicechat Paused by {checking}!")


@Client.on_message(command(["resume", "lanjut"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    checking = message.from_user.mention
    chat_id = message.chat.id
    if not await is_active_chat(chat_id):
        return await message.reply_text(
            "I dont think if something's playing on voice chat"
        )
    elif await is_music_playing(chat_id):
        return await message.reply_text(
            "I dont think if something's playing on voice chat"
        )
    else:
        await music_on(chat_id)
        await callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text(f"🎧 Voicechat Resumed by {checking}!")


@Client.on_message(command(["end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    checking = message.from_user.mention
    chat_id = message.chat.id
    if await is_active_chat(chat_id):
        try:
            clear(chat_id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text(f"🎧 kontol di end sama {checking}!")
    else:
        return await message.reply_text(
            "I dont think if something's playing on voice chat"
        )


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    checking = message.from_user.mention
    chat_id = message.chat.id
    chat_title = message.chat.title
    if not await is_active_chat(chat_id):
        await message.reply_text("Nothing's playing on Music")
    else:
        task_done(chat_id)
        if is_empty(chat_id):
            await remove_active_chat(chat_id)
            await message.reply_text("No more music in Queue \n\nLeaving Voice Chat")
            await callsmusic.pytgcalls.leave_group_call(chat_id)
            return
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id,
                InputStream(
                    InputAudioStream(
                        get(chat_id)["file"],
                    ),
                ),
            )
            await message.reply_text("⏭ **You've skipped to the next song.**")


@Client.on_message(filters.command("reload"))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_text("✅️ **ybg**")


@Client.on_message(filters.command("cleandb"))
@errors
@authorized_users_only
async def stop_cmd(_, message):
    chat_id = message.chat.id
    try:
        clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)
    try:
        await callsmusic.pytgcalls.leave_group_call(chat_id)
    except:
        pass
    await message.reply_text("Erased Databae, Queues, Logs, Raw Files, Downloads.")
