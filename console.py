from app import frequency_analysis_generator
import cmd

class WordFrequencyToolCommand(cmd.Cmd):
    prompt = ">>> "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True 


    def do_EOF(self, args):
        """EOF to exit the program"""
        print()
        return True 


    def emptyline(self):
        """Empty lines are ignored"""
        pass


    def preloop(self):
        print('/************************************************************/')
        print('/* Hello!                                                   */')
        print('/* This tool analyses a given text document and             */')
        print('/* provide insights into the frequency of words used in it. */')
        print('/* insights into the frequency of words used in it.         */')
        print('/*                                                          */')
        print('/* type `help` into the prompt to get all available commands*/')
        print('/* eg: >>> help                                             */')
        print('/*                                                          */')
        print('/* type help <command> to get the command requirements      */')
        print('/* eg: >>> help get_all                                     */')
        print('/************************************************************/')


    def do_get_all(self, args):
        """
            get all words and their frequencies
            takes argument: file path
            >>> get_all <path to file>
        """
        if len(args) < 1:
          print('usage: get_all <path to file>')
          return

        for value in frequency_analysis_generator(args):
            print(value)
        
    
    def do_get_max(self, args):
        """
            get the word with the maximum occurance in the file
            takes arguments: file path
            >>> get_max <path to file>
        """
        if len(args) < 1:
            print('usage: get_max <path to file>')
            return

        for value in frequency_analysis_generator(args):
           for key, val in value.items():
            if val == max(value.values()):
                print({key: val})
        

    def do_get_min(self, args):
        """
            get the word with the miminum occurance in the file
            takes arguments: file path
            >>> get_min <path to file>
        """
        if len(args) < 1:
          print('usage: get_min <path to file>')
          return 

        for value in frequency_analysis_generator(args):
            for key, val in value.items():
                if val == min(value.values()):
                    print({key: val})        


if __name__ == '__main__':
    WordFrequencyToolCommand().cmdloop()