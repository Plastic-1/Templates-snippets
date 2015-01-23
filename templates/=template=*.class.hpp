
#ifndef %GUARD%
# define %GUARD%

class	%CLASS% {

	public:
		%CLASS%(void);
		%CLASS%(%CLASS const & src);
		%CLASS%	operator=(%CLASS const & rhs);
		~%CLASS%(void);

	private:
		%HERE%

};

#endif /* !%GUARD% */
