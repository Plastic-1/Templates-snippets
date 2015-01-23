#include "%FILE%.class.hpp"
%HERE%
%CLASS%::%CLASS%(void) {
	return;
}

%CLASS%::%CLASS%(%CLASS% const & src) {
	*this = src;
	return;
}

%CLASS%&	%CLASS%::operator=(%CLASS% const & rhs) {
	(void)rhs;
	return *this;
}

%CLASS%::~%CLASS%(void) {
	return;
}
