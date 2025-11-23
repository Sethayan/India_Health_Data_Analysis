// Change large numbers to indian number system of daily usage
function formatNumber(num) {
    if (num >= 10000000) {
        return (num / 10000000).toFixed(1) + ' Cr';
    } else if (num >= 100000) {
        return (num / 100000).toFixed(1) + ' L';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toLocaleString();
}

// Graph labels are very long for some states. Need them to truncated
function truncateLabel(label, maxLength = 15) {
    if (label && label.length > maxLength) {
        return label.substring(0, maxLength) + '...';
    }
    return label;
}