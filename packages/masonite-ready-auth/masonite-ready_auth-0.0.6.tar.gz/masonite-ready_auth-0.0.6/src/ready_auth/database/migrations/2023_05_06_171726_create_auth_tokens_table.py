"""CreateAuthTokensTable Migration."""

from masoniteorm.migrations import Migration


class CreateAuthTokensTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("auth_tokens") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("auth_tokens")
