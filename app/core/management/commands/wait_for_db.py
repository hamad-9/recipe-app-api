"""
Django command to wait for database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""
    def handle(self, *args, **options):
        """entry point for command"""
        self.stdout.write('waiting for database...')
        dp_up = False
        while dp_up is False:
            try:
                self.check(databases=['default'])
                dp_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write('Database Unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
