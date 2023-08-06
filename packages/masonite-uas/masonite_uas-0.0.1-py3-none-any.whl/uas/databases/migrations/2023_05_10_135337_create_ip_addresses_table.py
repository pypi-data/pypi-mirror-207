"""CreateIpAddressesTable Migration."""

from masoniteorm.migrations import Migration


class CreateIpAddressesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("ip_addresses") as table:
            table.big_increments("id")
            table.string("address", 39).unique() 
            table.big_integer("visit_count").unsigned()
            table.timestamp("last_visit_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("ip_addresses")
