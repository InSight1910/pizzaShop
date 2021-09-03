import styled from "styled-components";
import PropTypes from "prop-types";
import { rem } from "../hooks/rem";

export const Icon = styled.img`
	width: ${({ width }) => rem(width)}rem;
`;
Icon.propTypes = {
	width: PropTypes.number,
};
export const Typographic = styled.h1`
	${({ fontSize }) => fontSize && `font-size: ${rem(fontSize)}rem`};
	${({ fontWeight }) => fontWeight && `font-weight: ${fontWeight}`};
	${({ color }) => color && `color: var(--color-${color})`};
	${({ lineHeight }) => lineHeight && `line-height: ${rem(lineHeight)}rem`};
	${({ margin }) => margin && `margin: ${margin}`};
`;

Typographic.propTypes = {
	fontSize: PropTypes.number,
	fontWeight: PropTypes.number,
	color: PropTypes.string,
	lineHeight: PropTypes.number,
};

export const Image = styled.img`
	display: block;
	${({ marginX, marginY, imgCenter }) =>
		imgCenter || marginX
			? `margin: ${rem(marginX)}rem auto;}`
			: `margin: ${rem(marginX)}rem ${rem(marginY)}rem;}`}
	width: ${({ width }) => rem(width)}rem;
	${({ borderRadius }) =>
		borderRadius && `border-radius: ${rem(borderRadius)}rem`};
`;
Image.propTypes = {
	marginX: PropTypes.number,
	marginY: PropTypes.number,
	width: PropTypes.number,
	borderRadius: PropTypes.number,
};
Image.defaultProps = {
	marginX: 0,
	marginY: 0,
};
