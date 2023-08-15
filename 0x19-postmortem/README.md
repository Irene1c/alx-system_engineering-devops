# Postmortem: WordPress Website Outage

## Issue Summary
- **Duration:** Start: August 9, 2023, 07:30 AM (GMT+0) | End: August 9, 2023, 07:35 AM (GMT+0)
- **Impact:** Internal Server Error (HTTP 500) | Users experienced inaccessibility to the WordPress website for approximately 5 minutes. 100% of users were affected.
- **Root Cause:** Spelling error in file path leading to a required PHP file.

## Timeline
* **07:30 AM:** Issue detected as users reported encountering "500 Internal Server Error" when attempting to access the WordPress website.
* **07:31 AM:** Initial investigation focused on the server logs and Apache error logs to identify the cause of the error.
* **07:32 AM:** Review of Apache error logs revealed the specific error related to a failed inclusion of the `class-wp-locale-switcher.phpp` file.
* **07:33 AM:** The assumption was made that a recent code change might have introduced the issue, leading to further review of recent commits.
* **07:34 AM:** Debugging effort shifted to inspecting the relevant code files to identify the root cause of the failed inclusion.
* **07:34 AM:** Escalation to senior developer for a second opinion on the debugging process.
* **07:35 AM:** Root cause identified: Spelling error in the file path (`class-wp-locale-switcher.phpp` instead of `class-wp-locale-switcher.php`).
* **07:35 AM:** Immediate fix applied by modifying the file path in the `wp-settings.php` file.

## Root Cause and Resolution
- **Root Cause:** Spelling error in file path caused PHP interpreter failure.
- **Resolution:** Corrected file path in `wp-settings.php`.

## Corrective and Preventative Measures
1. **Code Review and Testing:** Implement a stringent code review process to catch syntax errors and typos before deploying changes.
2. **Automated Testing:** Introduce automated unit tests and integration tests to validate code changes and catch errors during the development process.
3. **Documentation and Naming Conventions:** Maintain clear and consistent naming conventions for files and variables, and ensure that relevant documentation is up to date.
4. **Monitoring and Alerting:** Set up monitoring and alerting for critical server errors to detect and respond to issues promptly.
5. **Version Control Best Practices:** Enforce best practices for version control, including using branches for feature development and thoroughly reviewing code before merging.

## Key Takeaway
**Key Takeaway:** In the realm of coding, even a small typo can lead to unexpected chaos. Just like a pianist hitting a wrong note, a misspelled file path can cause the entire performance to fall flat.

![The Girl Plays The Piano Badly At The Concert Vector](https://media.istockphoto.com/id/1321094317/vector/the-girl-plays-the-piano-badly-at-the-concert-vector-illustration.jpg?s=1024x1024&w=is&k=20&c=cgLYP54iLkPF_m-9fxpDjAgCWbM9XR5KMpoc7MQH81I=)
