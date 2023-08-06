"""CreateUserAgentsTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserAgentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_agents") as table:
            table.big_increments("id")
            table.string("name", 39).unique() 
            table.big_integer("visit_count").unsigned()
            table.timestamp("last_visit_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_agents")
