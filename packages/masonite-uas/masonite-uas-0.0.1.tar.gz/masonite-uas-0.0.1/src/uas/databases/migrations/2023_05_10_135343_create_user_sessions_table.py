"""CreateUserSessionsTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserSessionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_sessions") as table:
            table.uuid("id").primary()
            table.uuid("session_id")
            table.foreign("session_id").references("id").on("session_users") 
            table.big_integer("visit_count").unsigned() 
            table.timestamp("last_visit_at")
            table.timestamps()  

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_sessions")
