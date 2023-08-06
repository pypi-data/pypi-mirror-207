"""CreateAccessLocationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccessLocationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("access_locations") as table:
            table.uuid("id").primary()
            table.uuid("user_session_id")
            table.foreign("user_session_id").references("id").on("user_sessions")
            table.uuid("ip_address_id")
            table.foreign("ip_address_id").references("id").on("ip_addresses") 
            table.big_integer("visit_count").unsigned()
            table.timestamp("completed_at")
            table.timestamp("expires_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("access_locations")
