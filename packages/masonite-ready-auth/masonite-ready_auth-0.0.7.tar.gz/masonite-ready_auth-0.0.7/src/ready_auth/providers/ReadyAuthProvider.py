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
                    "database/migrations/drop_conflicting_tables.py", 
                    "database/migrations/create_ip_addresses_table.py", 
                    "database/migrations/create_user_agents_table.py", 
                    "database/migrations/create_auth_tokens_table.py", 
                    "database/migrations/create_user_tokens_table.py", 
                    "database/migrations/create_users_table.py", 
                    "database/migrations/create_user_sessions_table.py", 
                    "database/migrations/create_access_locations_table.py", 
                    "database/migrations/create_personal_access_tokens_table.py"
                )

        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
