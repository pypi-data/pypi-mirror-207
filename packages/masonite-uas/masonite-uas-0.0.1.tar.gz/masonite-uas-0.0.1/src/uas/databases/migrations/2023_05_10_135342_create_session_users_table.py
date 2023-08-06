"""CreateSessionUsersTable Migration."""

from masoniteorm.migrations import Migration


class CreateSessionUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("session_users") as table:
            table.uuid("id").primary()
            table.big_integer("user_id").unsigned() 
            table.foreign("user_id").references("id").on("users")
            table.big_integer("visit_count").unsigned()
            table.timestamp("last_visit_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("session_users")
