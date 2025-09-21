# Event Processing System

A Python-based event processing system that manages events in a queue using a linked list data structure. This system provides a command-line interface for adding, processing, canceling, and displaying events with colorful terminal output.

## Description

This event processing system implements a First-In-First-Out (FIFO) queue using a custom linked list implementation. Events are processed in the order they were added, making it suitable for task scheduling, event handling, and workflow management applications.

## Features

- **Add Events**: Queue new events for processing
- **Process Events**: Handle events in FIFO order
- **Cancel Events**: Remove specific events from the queue
- **Display Events**: View all pending events in the queue
- **Colorful Interface**: Terminal output with color coding for better user experience
- **Error Handling**: Input validation and error messages

## Installation

### Prerequisites

- Python 3.6 or higher
- `colorama` library for colored terminal output

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/event-processing-system.git
cd event-processing-system
```

2. Install required dependencies:
```bash
pip install colorama
```

## Usage

Run the event processing system:

```bash
python Event_processing_system.py
```

### Menu Options

The system provides an interactive menu with the following options:

1. **Add event** - Add a new event to the processing queue
2. **Process event** - Process the next event in the queue (removes it from queue)
3. **Cancel event** - Remove a specific event from the queue
4. **Display events** - Show all events waiting to be processed
5. **Exit the system** - Close the application

### Example Usage

```
1. Add event
2. Process event
3. Cancel event
4. Display events
5. Exit the system
Enter your operation: 1
Enter event: Meeting with client
Meeting with client event is added to the queue

Enter your operation: 1
Enter event: Code review
Code review event is added to the queue

Enter your operation: 4
Displaying event waiting to be processed

Event Meeting with client waiting to be processed
Event Code review waiting to be processed

Enter your operation: 2
event Meeting with client has been processed
```

## Code Structure

### Classes

#### `event`
- **Purpose**: Represents a single event node in the linked list
- **Attributes**:
  - `data`: The event data/description
  - `next`: Pointer to the next event in the queue

#### `eventProcess`
- **Purpose**: Main class that manages the event processing system
- **Methods**:
  - `__init__()`: Initializes the event processor with an empty head node
  - `Addevent(data)`: Adds a new event to the end of the queue
  - `process()`: Processes (removes) the first event from the queue
  - `display()`: Shows all events currently in the queue
  - `cancel(data)`: Removes a specific event from the queue

### Color Coding

The system uses different colors to enhance user experience:
- **Green**: Success messages (event added, processed, cancelled)
- **Red**: Error messages (no events, invalid input)
- **Blue**: Information display (showing events)
- **Cyan**: Menu options
- **Yellow**: Exit message

## Requirements

Create a `requirements.txt` file:

```
colorama>=0.4.4
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Technical Details

- **Data Structure**: Custom linked list implementation
- **Queue Type**: FIFO (First-In-First-Out)
- **Memory Management**: Dynamic node allocation
- **Input Validation**: Handles invalid menu selections and input types

## Known Issues

- The cancel method may have edge cases when trying to cancel the last item
- No persistence - events are lost when the program exits
- No event priority system implemented

## Future Enhancements

- [ ] Add event priorities
- [ ] Implement event persistence (save/load from file)
- [ ] Add timestamps to events
- [ ] Implement event scheduling with time delays
- [ ] Add event categories or tags
- [ ] Create a web-based interface

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Project Link: [https://github.com/yourusername/event-processing-system](https://github.com/yourusername/event-processing-system)

## Acknowledgments

- Built using Python's standard library
- Colorama library for cross-platform colored terminal output
- Inspired by classic data structure implementations
