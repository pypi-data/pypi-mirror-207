"""PrepareUasTable Migration."""

from masoniteorm.migrations import Migration


class PrepareUasTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_table_if_exists("users")
        self.schema.drop_table_if_exists("password_resets")

    def down(self):
        """
        Revert the migrations.
        """
        pass