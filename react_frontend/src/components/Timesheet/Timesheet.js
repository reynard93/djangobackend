import React from 'react';
import './TimeSheet.css';


export default function Timesheet({children}) {
    return (
        <div className='sheet-container'>
            {children}
        </div>
    )
}

Timesheet.Profile = function TimeSheetProfile({children, ...restProps}) {
    return (
        <div {...restProps}>
            {children}
        </div>
    )
}

Timesheet.TimeDisplay = function TimesheetTimeDisplay({children, ...restProps}) {
    return (
        <div {...restProps} className='time-display'>
            {children}
        </div>
    )
}

Timesheet.Clock = function TimesheetClock({children, ...restProps}) {
    return (
        <div {...restProps}>
            {children}
        </div>
    )
}

Timesheet.Button = function TimesheetButton({children, ...restProps}) {
    return (
        <button {...restProps}>
            {children}
        </button>
    )
}

Timesheet.Error = function TimesheetError({children, ...restProps}) {
    return (<div {...restProps} className='error'>
        {children}
    </div>)
}