"""CreateProfiles Migration."""

from masoniteorm.migrations import Migration


class CreateProfiles(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("profiles") as table:
            table.increments("id")
            table.big_integer("users").unsigned() 
            table.string("first_name", 255).nullable()
            table.string("middle_name", 255).nullable() 
            table.string("last_name", 255).nullable() 
            table.string("gender", 64).nullable() 
            table.datetime("birthdate") 
            table.integer("country_id").nullable() 
            table.foreign("country_id").references("id").on("")
            table.string("phone").nullable() 
            table.string("bio", 1024).nullable()
            table.string("address", 512).nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("profiles")
