function housingRule(state) {
    if (state.playerStats.popFree <= 3) {
        alarms.housing.enable();
    } else {
        alarms.housing.disable();
    }
}