from datetime import datetime

class Stats:
    def __init__(self, command, id):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()
        # self.print_stats()

    def get_duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        print('\nid: {}'.format(self.id))
        print('command: {}'.format(self.command))
        print('response: {}'.format(self.response))
        print('start time: {}'.format(self.start_time))
        print('end_time: {}'.format(self.end_time))
        print('duration: {}\n'.format(self.duration))

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        sentence = ''
        sentence +=  '\nid: ' + str(self.id) + '\n'
        sentence += 'command: ' + str(self.command) + '\n'
        sentence += 'response: ' + str(self.response) + '\n'
        sentence += 'start time: ' + str(self.start_time) + '\n'
        sentence += 'end_time: ' + str(self.end_time) + '\n'
        sentence += 'duration: ' + str(self.duration) + '\n'
        return sentence
