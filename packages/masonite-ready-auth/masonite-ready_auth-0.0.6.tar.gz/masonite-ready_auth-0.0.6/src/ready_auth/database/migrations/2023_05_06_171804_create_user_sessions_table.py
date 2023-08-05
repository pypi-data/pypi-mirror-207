"""CreateUserSessionsTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserSessionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_sessions") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_sessions")
