"""CreatePendingLoginsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePendingLoginsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("pending_logins") as table:
            table.uuid("id").primary() 
            table.uuid("tfa_token_id")
            table.foreign("tfa_token_id").references("id").on("user_tokens")
            table.big_integer("ip_address_id").unsigned()
            table.foreign("ip_address_id").references("id").on("ip_addresses")
            table.timestamp("completed_at") 
            table.timestamp("expires_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("pending_logins")
