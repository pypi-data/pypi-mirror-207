"""CreateUsersTable Migration."""

from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.big_increments("id")
            table.string("username", 32).unique() 
            table.string("password", 255)
            table.string("email", 255).unique() 
            table.boolean("is_admin").default(False)
            table.string("avatar") 
            table.big_integer("registration_ip") 
            table.foreign("registration_ip").references("id").on("ip_addresses") 
            table.big_integer("visit_count")
            table.timestamp("last_visit_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
