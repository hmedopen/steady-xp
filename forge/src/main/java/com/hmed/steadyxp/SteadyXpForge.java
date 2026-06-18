package com.hmed.steadyxp;

import com.hmed.steadyxp.config.SteadyXpConfig;
import net.minecraftforge.fml.common.Mod;

@Mod(SteadyXpForge.MOD_ID)
public final class SteadyXpForge {
    public static final String MOD_ID = "steady_xp";

    public SteadyXpForge() {
        SteadyXpConfig.load();
    }
}
