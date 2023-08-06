"""CreateEmailTokensTable Migration."""

from masoniteorm.migrations import Migration


class CreateEmailTokensTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("email_tokens") as table:
            table.uuid("id").primary()
            table.string("type", 64)
            table.string("email")
            table.string("token", 5)
            table.timestamp("expires_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("email_tokens")
