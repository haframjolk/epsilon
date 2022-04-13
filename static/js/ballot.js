"use strict";
{
    /**
     * Counts how many checkboxes are checked in a group
     * 
     * @param {HTMLInputElement[]} group Checkbox group to check
     * @returns {number} Number of checked checkboxes in group
     */
    function countChecked(group) {
        let cnt = 0;
        for (const checkbox of group) {
            if (checkbox.checked) {
                cnt++;
            }
        }
        return cnt;
    }

    /**
     * Disable or enable all unchecked checkboxes in a group
     * 
     * @param {HTMLInputElement[]} group Checkbox group to modify
     * @param {boolean} value true if checkboxes should be disabled, false otherwise
     */
    function setDisabled(group, value) {
        for (const checkbox of group) {
            if (!checkbox.checked) {
                checkbox.disabled = value;
            }
        }
    }

    /**
     * Event handler ran on every checkbox change event, makes sure user doesn't select more candidates than is allowed
     */
    function changeHandler() {
        const checked = countChecked(checkboxGroup);
        if (checked >= limit) {
            setDisabled(checkboxGroup, true);
        } else {
            setDisabled(checkboxGroup, false);
        }
    }

    // Get candiate limit injected by template
    const limit = window.EPSILON_CANDIDATE_LIMIT || 1;

    // Find the candidate input group
    const checkboxGroup = document.forms.ballot.candidate;
    // If limit is above 1 and checkboxes are used, add change handler to all checkboxes
    if (limit > 1) {
        for (const checkbox of checkboxGroup) {
            checkbox.addEventListener("change", changeHandler);
        }
    }
}
