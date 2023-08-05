"""A ReadyAuthProvider Service Provider."""

from masonite.packages import PackageProvider


class ReadyAuthProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self
                .root("ready_auth")
                .name("ready_auth")
                .config("config/ready_auth.py", publish=True)
                .migrations(
                    "tests/integrations/databases/migrations/2023_05_06_171516_drop_conflicting_tables.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171713_create_ip_addresses_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171721_create_user_agents_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171726_create_auth_tokens_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171731_create_user_tokens_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171737_create_users_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171804_create_user_sessions_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171821_create_access_locations_table.py", 
                    "tests/integrations/databases/migrations/2023_05_06_171859_create_personal_access_tokens_table.py"
                )

        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
