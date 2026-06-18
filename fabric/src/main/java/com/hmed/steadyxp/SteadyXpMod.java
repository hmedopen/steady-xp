package com.hmed.steadyxp;

import com.hmed.steadyxp.config.SteadyXpConfig;
import net.fabricmc.api.ModInitializer;

public final class SteadyXpMod implements ModInitializer {
    public static final String MOD_ID = "steady_xp";

    @Override
    public void onInitialize() {
        SteadyXpConfig.load();
    }
}
