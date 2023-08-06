"""CreateUserTokensTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserTokensTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_tokens") as table:
            table.uuid("id").primary()
            table.string("type", 64)
            table.big_integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.string("token", 5)
            table.timestamp("expires_at")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_tokens")
