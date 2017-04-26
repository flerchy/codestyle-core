def _message_handler_thread(self):
        self._nick_change_failed = []
        while self.running:
            msg = self._message_queue.get(True)
            text = msg.get_data()
            conn = msg.get_connection()
            args = text.replace("\r", "").replace("\n", "").split(" ")
            command = args[0].upper()
            command_args = args[1:]
            if command == "NICK":
                if len(command_args) < 1:
                    self._send_not_enough_parameters(conn, command)
                else:
                    ident = self._clients[conn].identifier if self._clients[conn].identifier else None
                    if not self._set_nick(conn, command_args[0], ident):
                        self._nick_change_failed.append(conn)
            elif command == "USER":
                if conn in self._clients:
                    if len(command_args) < 2:
                        self._send_not_enough_parameters(conn, command)
                    else:
                        ''''
                        self._send_lusers(conn)
                        self._clients[conn].real_name = command_args[:]
                        self._clients[conn].identifier = self._clients[conn].get_nick() + "!" + \
                                                               command_args[0] + "@" + self.name
                        '''
                        self._set_nick(conn, command_args[0], command_args[1])
                        self._send_motd(conn)
                else:  # Another way to identify is USER command.
                    if len(command_args) < 2:
                        self._send_not_enough_parameters(conn, command)
                    elif conn in self._nick_change_failed:
                        self._nick_change_failed.remove(conn)
                    else:
                        if self._set_nick(conn, command_args[0], command_args[1]):
                            self._clients[conn].identifier = self._clients[conn].get_nick() + "!" + \
                                command_args[0] + "@" + self.name
                            self._send_motd(conn)
            elif command == "PRIVMSG" or command == "NOTICE":
                if len(command_args) < 2:
                    self._send_not_enough_parameters(conn, command)
                else:
                    message_text = command_args[1] if not command_args[1][0] == ":" else \
                        text.replace("\r\n", "")[text.index(":")+1:]
                    src = self._clients[conn].get_identifier()
                    dest = command_args[0]
                    if not dest.startswith("#"):
                        for clnt in self._clients.values():
                            if clnt.nick == dest:
                                clnt.connection.send(
                                    ":%s %s %s :%s" % (src, command, dest, message_text)
                                )
                                break
                        else:
                            self._send_no_user(conn, dest)
                    else:
                        for chan in self._channels:
                            if chan.name == dest:
                                self._channel_broadcast(conn, chan, ":%s %s %s :%s" %
                                            (src, command, dest, message_text))
                                break
                        else:
                            self._send_no_user(conn, dest)
            elif command == "JOIN":
                if len(command_args) < 1:
                    self._send_not_enough_parameters(conn, command)
                elif not all(c in ALLOWED_CHANNEL for c in command_args[0]) and len(command_args[0]):
                    self._send_no_channel(conn, command_args[0])
                else:
                    for chan in self._channels:
                        if chan.name == command_args[0]:
                            chan.users += 1
                            self._clients[conn].channels.append(chan)
                            self._send_to_related(conn, ":%s JOIN %s" % (self._clients[conn].get_identifier(),
                                                                         chan.name), True)
                            self._send_topic(conn, chan)
                            self._send_names(conn, chan)
                    else:
                        chan = Channel(command_args[0], 1)
                        chan.users = 1  # We have a user, because we have created it!
                        self._channels.append(chan)
                        self._clients[conn].channels.append(chan)
                        self._clients[conn].send(":%s JOIN %s" % (self._clients[conn].get_identifier(),
                                                   command_args[0]))
            elif command == "PART":
                if len(command_args) < 1:
                    self._send_not_enough_parameters(conn, command)
                else:
                    for chan in self._channels:
                        if chan.name == command_args[0]:

                            self._send_to_related(conn, ":%s PART %s" % (self._clients[conn].get_identifier(),
                                                                         command_args[0]))
                            self._clients[conn].channels.remove(chan)
                            chan.users -= 1
                            break
...
