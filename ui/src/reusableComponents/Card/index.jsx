import { Card, IconGroup, IconItem } from "../../styledComponents/Card";

import pizza from "../../assets/img/pizza-png-15.png";
import heart from "../../assets/icons/HeartRed.svg";
import star from "../../assets/icons/Star 1.svg";
import { Image, Typographic } from "../../styledComponents/Global";
import { Container } from "../../styledComponents/Layout";

export const CardContainer = ({ pizzaOfTheDay }) => {
	console.log(pizzaOfTheDay);
	return (
		<Card pizzaOfTheDay={pizzaOfTheDay}>
			<Image src={pizza} width={138} imgCenter={true} marginX={24} />
			<Container margin="0 auto">
				<Typographic as="h2" color="title" fontSize={16} fontWeight={500}>
					Lorem, ipsum dolor.
				</Typographic>
				<Typographic as="h2" color="title" fontSize={16} fontWeight={400}>
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint, sunt.
				</Typographic>
				{!pizzaOfTheDay && (
					<IconGroup>
						<IconItem>
							<Image src={star} width={16} />

							<Typographic fontWeight={400} fontSize={12} as="p">
								4+
							</Typographic>
						</IconItem>
						<IconItem>
							<Image src={heart} width={16} />
						</IconItem>
					</IconGroup>
				)}
			</Container>
		</Card>
	);
};
