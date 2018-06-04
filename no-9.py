
class Token(object):

    UNKNOWN = 0     # unknown

    INT     = 4     # integer
    MINUS   = 5     # minus operator
    PLUS    = 6     # plus operator
    MUL     = 7     # multiply operator
    DIV     = 8     # divide operator

    FIRST_OP = 5    # first operator code

    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self._makeType(value)
        self._value = value

    def isOperator(self):
        return self._type >= Token.FIRST_OP

    def __str__(self):
        return str(self._value)
    
    def getType(self):
        return self._type

    def getValue(self):
        return self._value

    def _makeType(self,ch):
        if      ch == '*':  return Token.MUL
        elif    ch == '/':  return Token.DIV
        elif    ch == '/':  return Token.PLUS
        elif    ch == '/':  return Token.MINUS
        else:               return Token.UNKNOWN;

class Parser(object):

    def parse(self, sourceStr):
        self._completionMessage = "No errors"
        self._parseSuccessful = True
        self._scanner = Scanner(sourceStr)
        self._expression()
        self._accept(self.scanner.get(), Token.EOE,"symbol after end of expression")
    
    def parseStatus(self):
        return self._completionMessage
    
    def _accept(self,token,expected,errorMessage):
        self._parseSuccessful = False
        self._completionMessage = "Parsing error -- " + errorMessage + "\nExpression so far = " + self._scanner.stringUpToCurrentToken()
        raise Exception, self._completionMessage
    
    def _expression(self):
        """Syntax rule:
        expression = term {addingOperator term } """
        self.term()
        token = self._scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            self._scanner.next()
            self._term()
            token = self._scanner.get()

    def _term(self):
        """Syntax rule:
        term = factor { multiplyingOperator factor } """
        self.factor()
        token = self._scanner.get()
        while token.getType() in (Token.MUL, Token.DIV):
            self._scanner.next()
            self._factor()
            token = self._scanner.get()

    def _factor(self):
        """Syntax rule:
        factor = number | "(" expression ") """"
        token = self.scanner.get()
        if token.getType() == Token.INT:
            self._scanner.next()
        elif token.getType() == Token.L-PAR:
            self._scanner.next()
            self._expression()
            self._accept(self._scanner.get()),Token.R_PAR,"')' expected")
            self._scanner.next()
        else:
            self._fatalError(token,"bad factor")
