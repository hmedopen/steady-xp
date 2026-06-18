package com.hmed.steadyxp.mixin;

import com.hmed.steadyxp.config.SteadyXpConfig;
import net.minecraft.world.entity.player.Player;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Overwrite;

@Mixin(value = Player.class, remap = false)
public abstract class PlayerMixin {
    /**
     * Makes the XP bar use the configured fixed cost at every level.
     *
     * @author hmed
     * @reason Steady XP replaces only the vanilla per-level curve.
     */
    @Overwrite(remap = false)
    public int getXpNeededForNextLevel() {
        return SteadyXpConfig.xpPerLevel();
    }
}
