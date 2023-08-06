"""A UASProvider Service Provider."""

from masonite.packages import PackageProvider



import os

class UASProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        self.root("uas") \
            .name("uas") \

        # REGISTER CONFIGURATION #
        self.config("config/uas.py", publish=True)

        # REGISTER CONTROLLERS # 
        self.controllers("controllers") 

        # REGISTER ROUTES # 
        self.routes("routes/web.py")

        # REGISTER MIGRATIONS
        migrations_folder = "uas/databases/migrations"
        migration_files = os.listdir(migrations_folder)
        self.migrations(*list(map(lambda migration_file: migrations_folder + "/" + migration_file, migration_files)))

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
