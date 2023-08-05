"""CreatePersonalAccessTokensTable Migration."""

from masoniteorm.migrations import Migration


class CreatePersonalAccessTokensTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("personal_access_tokens") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("personal_access_tokens")
