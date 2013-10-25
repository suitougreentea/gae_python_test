#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
import os
import cgi
from google.appengine.ext.webapp import template
from google.appengine.ext import db

import webapp2

class TestDB(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

# User mypage (redirect to User Class)
class MainHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    # if user:
    #   self.response.write(user)
    # else:
    #   self.redirect(users.create_login_url(self.request.uri))

    template_values = {
            'user': user,
            }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

# Register
class RegisterHandler(webapp2.RequestHandler):
  def get(self):
    self.response.set_status(403)
    # self.response.write('INPUT')
  def post(self):
    tdb = TestDB()

    if users.get_current_user():
        tdb.author = users.get_current_user()

    tdb.content = self.request.get('content')
    tdb.put()

    self.response.write(self.request.get('content'))

# View database
class ViewHandler(webapp2.RequestHandler):
  def get(self):
    tdbs = db.GqlQuery("SELECT * FROM TestDB ORDER BY date DESC LIMIT 10")

    for tdb in tdbs:
      if tdb.author:
        self.response.out.write('%s : ' % tdb.author.nickname())
      else:
        self.response.out.write('Anonymous : ')
      self.response.out.write('%s' % cgi.escape(tdb.content))


# Like Twitter url mapping is best
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/register', RegisterHandler),
  ('/view', ViewHandler),
], debug=True)