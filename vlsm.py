import re

# ------------------------------------------------------------------[ CLASS.ES ]

class Byte():
	def __init__(
		self,
		value: int
	):
		if value < 0 or value > 255:
			raise ValueError( f"{value}:invalid byte" )
		self.__value: int = value
	
	def GetValue( self ) -> int:
		return self.__value
	
	def GetBits( self ):
		return bin( self.__value )[2:]

class IpAddress():
	@staticmethod
	def validate_address( ip_address: str )-> bool:
		byte_pat = r"25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d"
		ip_pat = (
			fr"^(?P<byte1>{byte_pat})\." +
			fr"(?P<byte2>{byte_pat})\." +
			fr"(?P<byte3>{byte_pat})\." +
			fr"(?P<byte4>{byte_pat})$"
		)
		if re.match(ip_pat, ip_address) is None:
			raise ValueError( f"{ip_address}: invalid IP address." )

	def __init__(
		self,
		ip_address: str
	):
		IpAddress.validate_address( ip_address )
		bytes = ip_address.split( '.', 4 )
		self.__bytes: list[Byte] = []
		for i in bytes:
			self.__bytes.append( Byte( int( i ) ) )

# ----------------------------------------------------------------------[ MAIN ]

def main():
	try :
		ip = IpAddress( "12.254.123.56" )
	except ValueError as f:
		print( f )

if __name__ == "__main__":
	main()
