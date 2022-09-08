# Log4A - Log 4 Aggregation - A Basic Forensic Logging Tool

## Basic Features
Log4A allows you to quickly collect logs based on a time frame. It also is a modular system that allows you to implement "collectors" that collect different types of logs.

### Collectors
Collectors are the actual code grabbing logs. There are two types of collectors implemented in Log4A. 

- General Collectors
- Timed Collectors

General collectors are not timed based. They are intended to quickly grab certain files for as desired for extraction.

Timed Collectors take two arguments: a begin_time and end_time, both being of datetime type. The collector takes these dates and then grabs the logs accordingly, only exporting the specified date range.

Collectors are easily added to Log4A. To create a new collector, you only need to add a file to the "collectors" folder, and create a function that runs your collector using either the @general_collector decorator, or the @timed_collector decorator. As noted above, Timed Collectors are expected to have a begin_time and end_time argument, both of datetime type. Your collector should grab the log desired and a has of the content and return them as a tuple of strings (hash, content), where they will be handled by Log4A and returned in a results directory created within the Log4A root folder.

Once these have been added as listed above, running the Log4A module will also include running your collector. You can see the collectors folder for examples of how collectors are implemented.