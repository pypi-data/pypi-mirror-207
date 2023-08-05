"""CreateAccessLocationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccessLocationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("access_locations") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("access_locations")
