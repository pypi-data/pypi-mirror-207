"""CreateIpAddressesTable Migration."""

from masoniteorm.migrations import Migration


class CreateIpAddressesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("ip_addresses") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("ip_addresses")
