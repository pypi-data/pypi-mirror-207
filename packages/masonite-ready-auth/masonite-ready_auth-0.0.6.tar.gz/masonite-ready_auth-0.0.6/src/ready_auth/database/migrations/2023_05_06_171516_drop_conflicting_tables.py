"""DropConflictingTables Migration."""

from masoniteorm.migrations import Migration


class DropConflictingTables(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("drop_conflictings") as table:
            self.schema.drop("password_rests")
            self.schema.drop("users")

    def down(self):
        """
        Revert the migrations.
        """
        pass
