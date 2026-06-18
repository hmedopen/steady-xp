package com.hmed.steadyxp.config;

import net.fabricmc.loader.api.FabricLoader;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class SteadyXpConfig {
    private static final int DEFAULT_XP_PER_LEVEL = 30;
    private static final Pattern VALUE_PATTERN = Pattern.compile("(?m)^\\s*xp_per_level\\s*=\\s*(-?\\d+)\\s*(?:#.*)?$");
    private static final Path CONFIG_PATH = FabricLoader.getInstance().getConfigDir().resolve("steady_xp.properties");
    private static int xpPerLevel = DEFAULT_XP_PER_LEVEL;

    private SteadyXpConfig() {
    }

    public static void load() {
        if (Files.exists(CONFIG_PATH)) {
            try {
                Matcher matcher = VALUE_PATTERN.matcher(Files.readString(CONFIG_PATH, StandardCharsets.UTF_8));
                if (matcher.find()) {
                    xpPerLevel = Math.max(1, Integer.parseInt(matcher.group(1)));
                }
            } catch (IOException | NumberFormatException ignored) {
                xpPerLevel = DEFAULT_XP_PER_LEVEL;
            }
        }
        save();
    }

    private static void save() {
        try {
            Files.createDirectories(CONFIG_PATH.getParent());
            Files.writeString(CONFIG_PATH,
                    "# XP required for every level. Minimum: 1.\n" +
                    "xp_per_level = " + xpPerLevel + "\n",
                    StandardCharsets.UTF_8);
        } catch (IOException ignored) {
            // Keep the in-memory default if the config directory is read-only.
        }
    }

    public static int xpPerLevel() {
        return xpPerLevel;
    }
}
