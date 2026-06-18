package com.hmed.steadyxp.mixin;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.damagesource.DamageSource;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(value = ServerPlayer.class, remap = false)
public abstract class ServerPlayerMixin {
    @Inject(method = "die", at = @At("HEAD"), remap = false)
    private void steadyXp$preventDeathXpDrop(DamageSource source, CallbackInfo ci) {
        ((ServerPlayer) (Object) this).skipDropExperience();
    }

    @Inject(method = "restoreFrom", at = @At("TAIL"), remap = false)
    private void steadyXp$restoreXpAfterDeath(ServerPlayer oldPlayer, boolean keepEverything, CallbackInfo ci) {
        ServerPlayer newPlayer = (ServerPlayer) (Object) this;
        newPlayer.experienceLevel = oldPlayer.experienceLevel;
        newPlayer.experienceProgress = oldPlayer.experienceProgress;
        newPlayer.totalExperience = oldPlayer.totalExperience;
    }
}
