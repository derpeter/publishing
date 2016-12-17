#!/bin/python3
#    Copyright (C) 2016  derpeter
#    derpeter@berlin.ccc.de
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from twitter import Twitter, OAuth
import logging
logging = logging.getLogger()


def send_tweet(ticket, token, token_secret, consumer_key, consumer_secret):
    logging.info("tweeting the release")
    # todo add more logic here. Also we should only tweet the master releases
    
    if ticket.profile_slug == "hd":
        target = "media.ccc.de and youtube"
    else:
        target = "media.ccc.de"
        
    msg = " has been released as " + ticket.profile_slug + " on " + target
    title = ticket.title
    if len(title) >= (160 - len(msg)):
        title = title[0:len(msg)]
    message = title + msg
    # todo switch to oauth2
    t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    ret = t.statuses.update(status=message)
    logging.debug(ret)
