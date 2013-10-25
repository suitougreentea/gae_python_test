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
from google.appengine.ext.webapp import template

import webapp2

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

# View user information(user/user_id)
class UserHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello user!')

# View rival list of user(rival/user_id)
class RivalHandler(webapp2.RequestHandler):
  def get(self):
      self.response.write('Hello rival!')

# Register user
class RegisterHandler(webapp2.RequestHandler):
  # if not user[google_user], redirect to register
  def get(self):
    self.response.write('fill inputs')
  def post(self):
    self.response.write('register in the content below')
  def register(self):
    self.response.write('Register finish. redirect to top.')

# Register data to manager
class UpdateHandler(webapp2.RequestHandler):
  # input JSON data to textarea
  def get(self):
    self.response.write('Please input your data')
  def post(self):
    self.response.write('Register below')
  def update(self):
    self.response.write('Register finish')

# Manage music data and user data
class AdminHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello admin!')

# Like Twitter url mapping is best
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/user', UserHandler),
  ('/rival', RivalHandler),
  ('/register', RegisterHandler),
  ('/update', UpdateHandler),
  ('/admin', AdminHandler),
], debug=True)