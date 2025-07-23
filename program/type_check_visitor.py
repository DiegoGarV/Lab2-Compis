from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType, CharType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    
    elif isinstance(left_type, (StringType, CharType)) and isinstance(right_type, (StringType, CharType)):
        return StringType()
    
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())
  
  def visitPower(self, ctx: SimpleLangParser.PowerContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError(f"Unsupported operand types for **: {left_type} and {right_type}")
    
  def visitComparison(self, ctx: SimpleLangParser.ComparisonContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if type(left_type) == type(right_type):
        return BoolType()
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return BoolType()
    else:
        raise TypeError(f"Unsupported operand types for comparison: {left_type} and {right_type}")
    
  def visitChar(self, ctx: SimpleLangParser.CharContext):
    return CharType()
