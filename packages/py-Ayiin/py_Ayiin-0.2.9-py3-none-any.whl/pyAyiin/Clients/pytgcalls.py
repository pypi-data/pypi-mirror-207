# py - Ayiin
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/pyAyiin >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/pyAyiin/blob/main/LICENSE/>.
#
# FROM py-Ayiin <https://github.com/AyiinXd/pyAyiin>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import asyncio
import os


from fipper import Client
from fipper.types import CallbackQuery, Message
from fipper.raw.functions.channels import GetFullChannel
from fipper.raw.functions.messages import GetFullChat
from fipper.raw.functions.phone import CreateGroupCall, EditGroupCallTitle
from fipper.raw.types import InputPeerChannel, InputPeerChat

from ..config import Var as Variable
from ..methods.queue import Queues

from .client import *

try:
    from pytgcalls.exceptions import GroupCallNotFoundError
except ImportError:
    pass
    GroupCallNotFoundError = None


Var = Variable()


class ClientCalls(object):
    async def StartAud(self, video_ids):
        if AYIIN1:
            try:
                await AYIIN1.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN1.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN2:
            try:
                await AYIIN2.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN2.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN3:
            try:
                await AYIIN3.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN3.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN4:
            try:
                await AYIIN4.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN4.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN5:
            try:
                await AYIIN5.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN5.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN6:
            try:
                await AYIIN6.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN6.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN7:
            try:
                await AYIIN7.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN7.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN8:
            try:
                await AYIIN8.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN8.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN9:
            try:
                await AYIIN9.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN9.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN10:
            try:
                await AYIIN10.group_call.start_audio(video_ids)
            except BaseException as ex:
                await AYIIN10.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
    
    async def StartVid(self, video_ids):
        if AYIIN1:
            try:
                await AYIIN1.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN1.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN2:
            try:
                await AYIIN2.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN2.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN3:
            try:
                await AYIIN3.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN3.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN4:
            try:
                await AYIIN4.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN4.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN5:
            try:
                await AYIIN5.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN5.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN6:
            try:
                await AYIIN6.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN6.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN7:
            try:
                await AYIIN7.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN7.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN8:
            try:
                await AYIIN8.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN8.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN9:
            try:
                await AYIIN9.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN9.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN10:
            try:
                await AYIIN10.group_call.start_video(video_ids)
            except BaseException as ex:
                await AYIIN10.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
    
    async def JoinVc(self, ids):
        if AYIIN1:
            try:
                await AYIIN1.group_call.join(ids)
            except BaseException as ex:
                await AYIIN1.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN2:
            try:
                await AYIIN2.group_call.join(ids)
            except BaseException as ex:
                await AYIIN2.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN3:
            try:
                await AYIIN3.group_call.join(ids)
            except BaseException as ex:
                await AYIIN3.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN4:
            try:
                await AYIIN4.group_call.join(ids)
            except BaseException as ex:
                await AYIIN4.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN5:
            try:
                await AYIIN5.group_call.join(ids)
            except BaseException as ex:
                await AYIIN5.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN6:
            try:
                await AYIIN6.group_call.join(ids)
            except BaseException as ex:
                await AYIIN6.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN7:
            try:
                await AYIIN7.group_call.join(ids)
            except BaseException as ex:
                await AYIIN7.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN8:
            try:
                await AYIIN8.group_call.join(ids)
            except BaseException as ex:
                await AYIIN8.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN9:
            try:
                await AYIIN9.group_call.join(ids)
            except BaseException as ex:
                await AYIIN9.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN10:
            try:
                await AYIIN10.group_call.join(ids)
            except BaseException as ex:
                await AYIIN10.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
    
    async def LeaveVc(self, video_ids):
        if AYIIN1:
            try:
                await AYIIN1.group_call.leave()
            except BaseException as ex:
                await AYIIN1.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN2:
            try:
                await AYIIN2.group_call.leave()
            except BaseException as ex:
                await AYIIN2.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN3:
            try:
                await AYIIN3.group_call.leave()
            except BaseException as ex:
                await AYIIN3.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN4:
            try:
                await AYIIN4.group_call.leave()
            except BaseException as ex:
                await AYIIN4.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN5:
            try:
                await AYIIN5.group_call.leave()
            except BaseException as ex:
                await AYIIN5.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN6:
            try:
                await AYIIN6.group_call.leave()
            except BaseException as ex:
                await AYIIN6.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN7:
            try:
                await AYIIN7.group_call.leave()
            except BaseException as ex:
                await AYIIN7.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN8:
            try:
                await AYIIN8.group_call.leave()
            except BaseException as ex:
                await AYIIN8.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN9:
            try:
                await AYIIN9.group_call.leave()
            except BaseException as ex:
                await AYIIN9.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )
        if AYIIN10:
            try:
                await AYIIN10.group_call.leave()
            except BaseException as ex:
                await AYIIN10.send_message(
                    Var.LOG_CHAT,
                    f'KESALAHAN: {ex}',
                )


class GroupCalls(ClientCalls, Queues):
    def __init__(self):
        self.chat_id = []
        self.clients = {}
        self.active_calls = []
        self.msgid_cache = {}
        self.play_on = {}
    
    async def TitleVc(self, client, m, title: str):
        peer = await client.resolve_peer(m.chat.id)
        if isinstance(peer, InputPeerChannel):
            chat = await client.send(GetFullChannel(channel=peer))
        if isinstance(peer, InputPeerChat):
            chat = await client.send(GetFullChat(chat_id=peer.chat_id))
        return await client.send(
            EditGroupCallTitle(
                call=chat.full_chat.call,
                title=title,
            )
        )

    async def StartVc(self, client, m, title=None):
        peer = await client.resolve_peer(m.chat.id)
        await client.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=client.rnd_id() // 9000000000,
            )
        )
        titt = title if title else "🎧 Ayiin Music 🎧"
        await self.TitleVc(client, m, title=titt)
    
    async def startCall(self, client, msg):
        if self.play_on:
            for chats in self.play_on:
                await self.play_on[chats].stop()
            self.play_on.clear()
            await asyncio.sleep(3)
        if msg.video:
            for chats in list(self.clients):
                if chats != msg.chat.id:
                    await self.clients[chats].stop()
                    del self.clients[chats]
            self.play_on.update({self._chat: client.group_call})
        if msg.chat.id not in self.active_calls:
            try:
                client.group_call.on_network_status_changed(
                    self.on_network_changed)
                client.group_call.on_playout_ended(self.playout_ended_handler)
                await client.group_call.join(msg.chat.id)
            except GroupCallNotFoundError as er:
                await msg.reply(er)
                dn, err = await self.StartVc(client, msg)
                if err:
                    return False, err
            except Exception as e:
                await msg.reply(e)
                return False, e
        return True, None

    async def on_network_changed(self, msg, call, is_connected):
        chats = msg.chat.id
        if is_connected:
            if chats not in self.active_calls:
                self.active_calls.append(chats)
        elif chats in self.active_calls:
            self.active_calls.remove(chats)

    async def playout_ended_handler(self, client, msg, call, source, mtype):
        if os.path.exists(source):
            os.remove(source)
        await self.play_from_queue(client, msg)

    async def play_from_queue(self, client, msg):
        chat_id = msg.chat.id
        if chat_id in self.play_on:
            await client.group_call.stop_video()
            self.play_on.pop(chat_id)
        try:
            ppk = await self.skip_song(chat_id)
            if ppk == 0:
                await self.LeaveVc()
            elif ppk == 1:
                await msg.reply("**Antrian Udah Kosong Tod, Gua Cabut Dari OS**")
            else:
                await msg.reply(
                        f"**• Memutar** - [{ppk[0]}]({ppk[1]}) | `{ppk[2]}`",
                        disable_web_page_preview=True,
                    )
        except Exception as e:
            await msg.reply(e)

    async def JoinVcg(self, client, msg):
        chat_id = msg.chat.id
        done, err = await self.startCall(client, msg)

        if done:
            return True
        await msg.reply(f"KESALAHAN saat Bergabung ke Obrolan Suara - {chat_id} :\n{err}")
        return False
                