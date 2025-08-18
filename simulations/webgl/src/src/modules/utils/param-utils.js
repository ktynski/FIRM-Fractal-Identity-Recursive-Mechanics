/**
 * Parameter Utilities
 * Safe parameter modification and user override tracking
 */

// Track user overrides to prevent automatic system changes
const userOverrides = new Set();

/**
 * Safely modify a parameter with protection against user overrides
 * @param {string} paramName - Name of the parameter
 * @param {number} newValue - New value to set
 * @param {string} reason - Reason for the modification (for logging)
 */
export function safeParamModify(paramName, newValue, reason = 'automatic system modification') {
  if (!window.params) return false;
  
  if (userOverrides.has(paramName)) {
    // User has manually changed this parameter, respect their choice
    return false;
  }
  
  // Safe to modify
  const oldValue = window.params[paramName];
  window.params[paramName] = newValue;
  
  if (Math.abs(oldValue - newValue) > 0.001) {
    console.log(`🔧 Auto-param: ${paramName} ${oldValue.toFixed(3)} → ${newValue.toFixed(3)} (${reason})`);
  }
  
  return true;
}

/**
 * Reset user overrides to allow automatic parameter changes again
 * @param {Array<string>} paramNames - Specific parameters to reset, or null for all
 */
export function resetUserOverrides(paramNames = null) {
  if (paramNames) {
    paramNames.forEach(param => userOverrides.delete(param));
    console.log(`🔓 Reset overrides for: ${paramNames.join(', ')}`);
  } else {
    userOverrides.clear();
    console.log('🔓 All parameter overrides reset - automatic changes re-enabled');
  }
}

/**
 * Mark a parameter as user-modified to prevent automatic changes
 * @param {string} paramName - Name of the parameter to protect
 */
export function markAsUserOverride(paramName) {
  userOverrides.add(paramName);
  
  // Also register with visual controller's manual override system if available
  const vc = window.simulationCore?.fsctfEngine?.visualController;
  if (vc && window.params && window.params[paramName] !== undefined) {
    vc.manualOverrides.set(paramName, {
      value: window.params[paramName],
      timestamp: Date.now(),
      source: 'user_ui_builder'
    });
    console.log(`🎛️ User override registered for ${paramName}: ${window.params[paramName]} (total: ${vc.manualOverrides.size})`);
  }
}

/**
 * Check if a parameter is protected by user override
 * @param {string} paramName - Name of the parameter to check
 * @returns {boolean} True if parameter is protected
 */
export function isUserOverride(paramName) {
  return userOverrides.has(paramName);
}

/**
 * Get all parameters currently protected by user overrides
 * @returns {Array<string>} Array of protected parameter names
 */
export function getUserOverrides() {
  return Array.from(userOverrides);
}

/**
 * Get count of protected parameters
 * @returns {number} Number of parameters protected by user overrides
 */
export function getOverrideCount() {
  return userOverrides.size;
}

// Export userOverrides set for external access if needed
export { userOverrides };
