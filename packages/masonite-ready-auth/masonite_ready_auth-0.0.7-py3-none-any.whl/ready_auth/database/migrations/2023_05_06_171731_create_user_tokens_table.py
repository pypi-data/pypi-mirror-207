"""CreateUserTokensTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserTokensTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_tokens") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_tokens")
