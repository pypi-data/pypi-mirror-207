"""CreateUserAgentsTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserAgentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_agents") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_agents")
