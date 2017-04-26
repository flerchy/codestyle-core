import logging
import os
import datetime

import gntp.notifier

from nose.plugins import Plugin
from pkg_resources import resource_string

log = logging.getLogger('nose.plugins.nose_gntp')
logging.getLogger("gntp").setLevel(logging.WARNING)

class Notifier():
  default_app_icon = resource_string('nose_gntp', 'info.png')
  success_icon = resource_string('nose_gntp', 'success.png')
  failure_icon = resource_string('nose_gntp', 'failed.png')

  def __init__(self):
    self.success = gntp.notifier.GrowlNotifier(
      applicationName = "Success!",
      notifications = ["New Updates","New Messages"],
      defaultNotifications = ["New Messages"]
    )

    self.success.register()

    self.default_app = gntp.notifier.GrowlNotifier(
      applicationName = "Tests",
      notifications = ["New Updates","New Messages"],
      defaultNotifications = ["New Messages"]
    )

    self.default_app.register()

    self.failure = gntp.notifier.GrowlNotifier(
      applicationName = "Failed!",
      notifications = ["New Updates","New Messages"],
      defaultNotifications = ["New Messages"]
    )

    self.failure.register()

  def notify(self, kind, title, description, sticky=False):
    attr = getattr(self, kind)
    icon = getattr(self, kind + "_icon")

    attr.notify(
      noteType = "New Messages",
      title = title,
      description = description,
      sticky = sticky,
      icon = icon,
      priority = 1,
    )


class NoseGntp(Plugin):
  name = 'gntp'

  def begin(self):
    self.start_time = datetime.datetime.now()
    Notifier().notify("default_app", "Started", "At: %s" % self.start_time.strftime("%H:%M"))
    
  def options(self, parser, env=os.environ):
    super(NoseGntp, self).options(parser, env=env)

  def configure(self, options, conf):
    super(NoseGntp, self).configure(options, conf)

    if not self.enabled:
      return

  def finalize(self, result):
    self.finish_time = datetime.datetime.now()
    delta = self.finish_time - self.start_time

    if result.wasSuccessful():
      Notifier().notify("success", "All tests passed!", "%s tests run OK in %s.%s seconds" % (result.testsRun, delta.seconds, delta.microseconds))
    else:
      Notifier().notify("failure", "Some tests failed!", "%s tests. %s failed. %s errors." % (result.testsRun, len(result.failures), len(result.errors)), True)
