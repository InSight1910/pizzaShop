import { Container, Header } from "../../styledComponents/Layout";
import { BottomBar, NavLink } from "../../styledComponents/BottomBar";
import { Icon } from "../../styledComponents/Global";

import Home from "../../assets/icons/Home.svg";
import Heart from "../../assets/icons/Heart.svg";
import Search from "../../assets/icons/Search.svg";
import Notification from "../../assets/icons/Notification.svg";
import Buy from "../../assets/icons/Buy.svg";

export const Navbar = () => {
	const icons = [
		{
			src: Home,
		},
		{
			src: Heart,
		},
		{
			src: Search,
			borderRadius: 50,
			background: "--gradient",
			center: true,
		},
		{
			src: Notification,
		},
		{
			src: Buy,
		},
	];
	return (
		<Header>
			<Container margin="auto">
				<BottomBar>
					{icons.map(({ src, borderRadius, background, center }, index) => (
						<NavLink
							key={index}
							href="#"
							background={background}
							borderRadius={borderRadius}
						>
							<Icon src={src} width={24} />
						</NavLink>
					))}
				</BottomBar>
			</Container>
		</Header>
	);
};
