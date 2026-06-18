# Steady XP

Steady XP replaces Minecraft's increasing XP curve with one predictable cost:
**30 XP per level by default**. XP drops and normal gameplay systems remain unchanged.

## Features

- Every level costs the same configurable amount of XP.
- The default is `30 XP` per level.
- XP is retained on death without enabling `keepInventory`; inventory still drops normally.
- No changes to mob or ore XP drops, bottles o' enchanting, enchanting, anvils, or Mending.
- Server-compatible: the mod is required on the server and works for connected players.

## Loader support

| Loader | Status | Source module |
|---|---|---|
| Fabric | Supported | [`fabric/`](fabric/) |
| NeoForge | Planned | Not added yet |
| Forge | Planned | Not added yet |

Future loaders will live in their own top-level modules while sharing this repository,
issue tracker, versioning, documentation, and release history.

## Configuration

The first launch creates `config/steady_xp.properties`:

```properties
xp_per_level = 30
```

The minimum accepted value is `1`. Existing config values are preserved when updating.

## Building

Steady XP currently targets Minecraft 26.1.2, Fabric Loader 0.19.3, and Java 25.

```powershell
.\gradlew.bat build
```

The Fabric JAR is written to `fabric/build/libs/` and is named with the loader,
for example `steady-xp-fabric-1.0.0.jar`.

## Links

- [Source code](https://github.com/hmedopen/steady-xp)
- [Issues and feature requests](https://github.com/hmedopen/steady-xp/issues)

## License

Steady XP is available under the [MIT License](LICENSE).
