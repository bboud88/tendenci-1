import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from tendenci.core.base.models import UpdateTracker

class Command(BaseCommand):
    """
    Update tendenci via pip and restarts the server
    """
    def handle(self, *args, **kwargs):
        print "Updating tendenci package"
        os.system('pip install tendenci --upgrade')

        print "Updating tendenci site"
        os.system('python deploy.py')

        print "Restarting Server"
        # This depends on the server used, please update accordingly
        os.system('reload tendencisite')
        os.system('service nginx restart')

        UpdateTracker.end()
        call_command('clear_cache')
